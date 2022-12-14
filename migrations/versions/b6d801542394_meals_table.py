"""meals table

Revision ID: b6d801542394
Revises: 
Create Date: 2022-08-30 13:11:58.879353

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b6d801542394'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meals',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('timestamp', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_meals_timestamp'), 'meals', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_meals_timestamp'), table_name='meals')
    op.drop_table('meals')
    # ### end Alembic commands ###
